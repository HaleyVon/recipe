# create_recipe_json.py

import json

def create_recipe_json():
    recipes = [
        {
            "id": 1,
            "source": "편스토랑",
            "name": "휴게소 버터감자",
            "total_time": "15분",
            "servings": "2인분",
            "ingredients": [
                {"name": "감자", "amount": "5~6개"},
                {"name": "버터", "amount": "40g"},
                {"name": "설탕", "amount": "1T"},
                {"name": "알룰로스", "amount": "1T"},
                {"name": "소금", "amount": "1T"},
                {"name": "물", "amount": "200ml"}
            ],
            "instructions": [
                {"order": "1", "howto":"감자 껍질을 벗기고 반으로 잘라 팬에 넣는다"},
                {"order": "2", "howto":"팬에 물 200ml 넣고 소금 뿌리고 중불로 끓인다"},
                {"order": "3", "howto":"물이 졸아들면 버터와 설탕을 넣고 약불로 줄인다"},
                {"order": "4", "howto":"뚜껑을 덮어 약불로 익히고, 중간중간 뒤집어서 골고루 묻게 한다"},
                {"order": "5", "howto":"10분 뒤 완성"}
            ],
            "image_url": "https://cdn.pixabay.com/photo/2013/07/13/10/21/dish-157037_1280.png",
            "tags": {
                "type": ["간식", "브런치"],
                "cuisine": ["한식"]
            }
        },
        {
            "id": 2,
            "source": "백종원의 요리비책",
            "name": "김치찌개",
            "total_time": "30분",
            "servings": "2인분",
            "ingredients": [
                {"name": "김치", "amount": "300g"},
                {"name": "돼지고기", "amount": "100g"},
                {"name": "두부", "amount": "1/2모"},
                {"name": "대파", "amount": "1대"},
                {"name": "고춧가루", "amount": "1T"},
                {"name": "다진 마늘", "amount": "1T"},
                {"name": "식용유", "amount": "1T"}
            ],
            "instructions": [
                {"order": "1", "howto":"김치를 적당한 크기로 자르고, 돼지고기는 얇게 썬다"},
                {"order": "2", "howto":"냄비에 식용유를 두르고 돼지고기를 볶는다"},
                {"order": "3", "howto":"김치를 넣고 함께 볶다가 물을 넣는다"},
                {"order": "4", "howto":"두부를 넣고 끓이다가 고춧가루, 다진 마늘을 넣는다"},
                {"order": "5", "howto":"대파를 넣고 조금 더 끓여 마무리한다"}
            ],
            "image_url": "https://example.com/kimchi-stew.jpg",
            "tags": {
                "type": ["메인요리"],
                "cuisine": ["한식"]
            }
        },
        {
            "id": 3,
            "source": "블로그",
            "name": "샐러드 우동",
            "total_time": "20분",
            "servings": "1인분",
            "ingredients": [
                {"name": "우동면사리", "amount": "1봉지 (파스타면, 메밀면도 가능)"},
                {"name": "방울토마토", "amount": "4-5개"},
                {"name": "냉동새우", "amount": "5마리"},
                {"name": "오이", "amount": "1/4개"},
                {"name": "양파", "amount": "1/4개"},
                {"name": "샐러드 채소", "amount": "한 줌"},
                {"name": "캔옥수수", "amount": "2-3숟가락"}
            ],
            "sauce": [
                {"name": "올리브오일", "amount": "3숟가락"},
                {"name": "진간장", "amount": "2숟가락"},
                {"name": "화이트발사믹식초", "amount": "2숟가락"},
                {"name": "알룰로스", "amount": "1-1.5숟가락"},
                {"name": "참기름", "amount": "1숟가락"},
                {"name": "다진 마늘", "amount": "0.5숟가락"},
                {"name": "홀그레인머스터드", "amount": "0.5숟가락"}
            ],
            "instructions": [
                {"order": "1", "howto": "우동면을 삶아 찬물에 헹궈 물기를 뺀다"},
                {"order": "2", "howto": "방울토마토는 반으로 자르고, 오이와 양파는 얇게 슬라이스한다"},
                {"order": "3", "howto": "냉동새우는 해동하여 끓는 물에 살짝 데친다"},
                {"order": "4", "howto": "볼에 소스 재료를 모두 넣고 잘 섞어 드레싱을 만든다"},
                {"order": "5", "howto": "큰 볼에 우동면, 준비한 채소, 새우, 캔옥수수를 넣고 드레싱을 부어 잘 버무린다"},
                {"order": "6", "howto": "접시에 담고 기호에 따라 후추를 뿌려 마무리한다"}
            ],
            "image_url": "https://example.com/salad-udon.jpg",
            "tags": {
                "type": ["브런치", "샐러드"],
                "cuisine": ["퓨전"]
            }
        }
    ]

    with open('recipes.json', 'w', encoding='utf-8') as f:
        json.dump(recipes, f, ensure_ascii=False, indent=4)
    print("JSON file with tags created successfully.")

if __name__ == "__main__":
    create_recipe_json()
