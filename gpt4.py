import json
import requests

def question(ask_box1, ask_box2, ask_box3, ask_box4):

        dangbu = " 조건2: 만약 글에 서철모 서구청장의 당부 내용이 누락되어 있는 경우, 글의 맥락에 적절하게 서철모 서구청장의 당부 내용을 창작하여 써주세요."
        
        
        ask = ("당신은 20년차 베테랑 신문기자입니다. 대전 서구를 위해 기사를 작성중입니다. 다음 내용을 아래의 조건에 맞추어 제목과 신문기사를 작성해주세요.  "
        + ask_box1 + " " + ask_box2 + " "  + ask_box3 + " "  + ask_box4 \
        + " 조건1: 다음 [예시문]의 글 형식과 말투를 분석한 후에 동일한 스타일로 써주세요.    + [예시문] 대전 서구(구청장 서철모) 월평1동 적십자봉사회(회장 김광일)는 관내 저소득층 50세대에 추석맞이 생필품 꾸러미 나눔 활동을 펼쳤다고 17일 밝혔다."\
        + dangbu + " 조건3: 제목은 2개인데 하나는 간결한 주 제목을 다른 하나는 조금 더 상세한 소 제목으로 작성해줘, 그리고 서철모를 지칭할때 항상 서철모 청장이라고 해줘")

        # ChatGPT API 엔드포인트 URL
        api_url = "https://api.openai.com/v1/chat/completions"

        # OpenAI API 키
        api_key = "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" #챗싯계정
        

        # 질문 설정
        question = ask

        # API 호출을 위한 요청 페이로드 설정
        payload = {
            "model": "gpt-4",
            "messages": [
                #{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
            "max_tokens": 2000,  # 각 응답의 최대 토큰 수 설정
            "temperature": 0.7,  # 다양성 조절을 위한 값 설정
            "n": 3  # 받고 싶은 답변의 수 설정 (하나의 답변만 필요)
        }

        # API 호출 실행
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(api_url, data=json.dumps(payload), headers=headers)

        # API 응답 확인
        if response.status_code == 200:
            data = response.json()
            answer1 = data['choices'][0]['message']['content']  
            answer2 = data['choices'][1]['message']['content']      
            answer3 = data['choices'][2]['message']['content'] 

                  
        else:
            print(f"API 호출 실패: {response.status_code}, {response.text}")

        return answer1 , answer2, answer3