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
            "source": "백종원의 요리비책",
            "name": "순두부찌개",
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
        }
    ]

    with open('recipes.json', 'w', encoding='utf-8') as f:
        json.dump(recipes, f, ensure_ascii=False, indent=4)
    print("JSON file with tags created successfully.")

if __name__ == "__main__":
    create_recipe_json()