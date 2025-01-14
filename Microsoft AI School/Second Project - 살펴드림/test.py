import os, json

from openai import AzureOpenAI
from datetime import datetime
from zoneinfo import ZoneInfo

# def get_current_time(location="Asia/Seoul"):
#     print(ZoneInfo(location))
#     current_time = datetime.now(ZoneInfo(location)).strftime("%Y-%m-%d %H:%M %p")
#     return current_time

# a = []
# a.insert(0, {"role": "system", "content": f"{get_current_time()}" + "B"})
# print(a)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "주어진 장소의 현재 시간 획득, 장소가 주어지지 않았다면 대한민국 서울을 기준으로 한다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "장소의 IANA TimeZone. 장소에 대한 정보가 없다면 기본값은 Asia/Seoul",
                    },
                },
                "required": ["location"],
            },
        }
    }
]

current_time = datetime.now(ZoneInfo("Asia/Seoul")).replace(microsecond=0)
print(current_time)
# client = AzureOpenAI(
#     azure_endpoint = "https://5b038-azure-openai.openai.azure.com/",
#     api_key="",  
#     api_version="2024-02-15-preview"
# )

# response = client.chat.completions.create(
#     model="gpt-4o", # model = "deployment_name".
#     messages=[
#         {
#             "role": "system",
#             "content": '''
#                     사용자는 전체 대화 기록을 너에게 제공한다.
#                     그리고 전체 대화 기록을 통해 기존에 만들어진 사용자의 일정 및 약속, 계획 등에 대한 json 리스트 데이터를 너에게 제공될 수도, 제공되지 않을 수도 있다. 
#                     너는 주어진 데이터에서 사용자의 일정 및 약속, 계획 등에 대한 것을 다음과 같이 json 리스트 형태로 정리하여야 한다.
#                     [{"date": date(yyyy-mm-dd),"time": time(hh:MM),"destination": str,"purpose": str,"is_done": bool}]
#                     그 외의 어떠한 출력도 허용되지 않는다.
#                 '''
#         },
#         {
#             "role": "user",
#             "content": "그 기억 하나만 해주소 딴 게 아니라 내가 11월 28일 9시에 병원 예약을 했다카이 기래갖고 그때 돼서 좀 알려주믄 좋겠구먼",
#             "time": "2024-11-26 14:35:07 PM"
#         },
#         {
#             "role": "assistant",
#             "content": "네, 2024년 11월 28일 오전 9시에 병원을 가셔야 하는군요. 예약 날짜 전에 다시 한번 알려드릴게요.",
#             "time": "2024-11-26 14:35:26 PM"
#         },
#         {
#             "role": "user",
#             "content": "안녕하신감",
#             "time": "2024-12-19 15:12:34 PM"
#         },
#         {
#             "role": "assistant",
#             "content": "안녕하세요, 무엇을 도와드릴까요?",
#             "time": "2024-12-19 15:12:37 PM"
#         },
#         {
#             "role": "user",
#             "content": "내일 오전 9시에 병원에 예약해놔가꼬 그리 간다야",
#             "time": "2024-12-19 15:12:57 PM"
#         },
#         {
#             "role": "assistant",
#             "content": "내일 오전 9시, 병원 예약 확인했습니다. 기억해 두어야 할 다른 일정도 있으신가요?",
#             "time": "2024-12-19 15:13:12 PM"
#         },
#         {
#             "role": "user",
#             "content": "다른 일정? 그 뭐 아 그거 있다 그거. 오후 1시쯤에 저기 거 점심 약속이 있는데 그 장소가 기억 안 난다 아무튼 점심 약속 있다.",
#             "time": "2024-12-19 15:13:40 PM"
#         },
#         {
#             "role": "assistant",
#             "content": "내일 오후 1시, 점심 약속 확인했습니다. 기억해 두어야 할 다른 일정도 있으신가요?",
#             "time": "2024-12-19 15:13:12 PM"
#         },
#         {
#             "role": "user",
#             "content": "없다",
#             "time": "2024-12-19 15:13:23 PM"
#         },
#         {
#             "role": "assistant",
#             "content": "네, 알겠습니다. 다른 도움 필요하신 게 있으신가요?",
#             "time": "2024-12-19 15:13:34 PM"
#         }
#     ]
# )

# # print(response.choices[0].message)
# print(response.choices[0].message.content)


response = client.chat.completions.create(
    model="gpt-4o", # model = "deployment_name".
    messages=[
        {
            "role": "system",
            "content": '''
                    사용자는 전체 대화 기록을 너에게 제공한다.
                    그리고 전체 대화 기록을 통해 기존에 만들어진 사용자의 일정 및 약속, 계획 등에 대한 json 리스트 데이터를 너에게 제공될 수도, 제공되지 않을 수도 있다. 
                    너는 주어진 데이터에서 사용자의 일정 및 약속, 계획 등에 대한 것을 다음과 같이 json 리스트 형태로 정리하여야 한다.
                    [{"date": date(yyyy-mm-dd),"time": time(hh:MM),"destination": str,"purpose": str,"is_done": bool}]
                    그 외의 어떠한 출력도 허용되지 않는다.
                '''
        },
        {
            "role": "user",
            "content": "그 기억 하나만 해주소 딴 게 아니라 내가 11월 28일 9시에 병원 예약을 했다카이 기래갖고 그때 돼서 좀 알려주믄 좋겠구먼",
            "time": "2024-11-26 14:35:07 PM"
        },
