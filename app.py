import streamlit as st
import json
from PIL import Image, ImageDraw
import requests
from io import BytesIO
import os
from create_recipe_json import create_recipe_json

# JSON 파일 로드 함수 (캐시 비활성화)
def load_data():
    json_file = 'recipes.json'
    if not os.path.exists(json_file):
        create_recipe_json()
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

# 이미지 로드 및 처리 함수
@st.cache_data
def load_and_process_image(url, size=(300, 240), corner_radius=15):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize(size, Image.LANCZOS)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([(0, 0), size], corner_radius, fill=255)
        img = img.convert("RGBA")
        rounded_img = Image.new("RGBA", size, (0, 0, 0, 0))
        rounded_img.paste(img, (0, 0), mask)
        return rounded_img
    except:
        return None

def main():
    st.set_page_config(page_title=":cook 오늘 집밥 레시피", layout="wide")

    # CSS 파일 로드
    with open('style.css', 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # 메인 타이틀
    st.markdown("<h1 class='main-title'>오늘 집밥 레시피</h1>", unsafe_allow_html=True)

    # 데이터 로드 (매번 새로 로드)
    recipes = load_data()

    # 모든 태그 추출
    all_tags = {}
    for recipe in recipes:
        for tag_type, tags in recipe['tags'].items():
            if tag_type not in all_tags:
                all_tags[tag_type] = set()
            all_tags[tag_type].update(tags)

    # 검색 및 필터링 섹션
    with st.expander("레시피 검색하기", expanded=False):
        search_query = st.text_input("레시피 또는 재료 검색:")
        
        # 태그 선택
        selected_tags = {}
        for tag_type, tags in all_tags.items():
            selected_tags[tag_type] = st.multiselect(f"{tag_type}", options=sorted(tags), key=f"{tag_type}_tags")

    # 레시피 필터링
    filtered_recipes = recipes
    if search_query:
        filtered_recipes = [
            recipe for recipe in filtered_recipes
            if search_query.lower() in recipe['name'].lower() or
            any(search_query.lower() in ingredient['name'].lower() for ingredient in recipe['ingredients'])
        ]
    
    for tag_type, selected in selected_tags.items():
        if selected:
            filtered_recipes = [
                recipe for recipe in filtered_recipes
                if any(tag in recipe['tags'][tag_type] for tag in selected)
            ]

    # 레시피 목록 섹션
    st.subheader("레시피를 선택하세요")
    for recipe in filtered_recipes:
        if st.button(f"{recipe['name']} ({recipe['total_time']})", key=str(recipe['id'])):
            st.session_state.selected_recipe = recipe['id']

    # 선택된 레시피 상세 정보
    if 'selected_recipe' in st.session_state:
        recipe = next((r for r in recipes if r['id'] == st.session_state.selected_recipe), None)
        if recipe:
            st.markdown("---")
            with st.container():
                st.markdown("<div class='recipe-details'>", unsafe_allow_html=True)
                st.title(recipe['name'])

                # 태그 표시
                tag_html = ""
                for tag_type, tags in recipe['tags'].items():
                    for tag in tags:
                        tag_class = f"tag-{tag_type}" if tag_type in ['type', 'cuisine', 'ingredient'] else "tag-other"
                        tag_html += f'<span class="tag-pill {tag_class}">{tag}</span>'
                st.markdown(tag_html, unsafe_allow_html=True)
                
                img = load_and_process_image(recipe['image_url'])
                if img:
                    st.image(img, use_column_width=False, width=300)
                
                st.code(f"출처: {recipe['source']}, 조리 시간: {recipe['total_time']}, 몇 인분: {recipe['servings']}")                

                # 재료
                st.subheader("재료")
                ingredients_data = [
                    {"재료": ingredient['name'], "양": ingredient['amount']}
                    for ingredient in recipe['ingredients']
                ]
                st.table(ingredients_data)

                # 조리 순서
                st.subheader("조리 순서")
                for instruction in recipe['instructions']:
                    st.write(f"{instruction['order']}. {instruction['howto']}")
                
                st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
