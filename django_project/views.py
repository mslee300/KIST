from django.shortcuts import render
import openai

from .forms import AnswerForm

# 여기에다 발급받은 API Key를 넣어주세요
openai.api_key = ""

# AI message generator
def generate_message(request, prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    # 여기에서 챗봇을 커스텀하세요
    messages=[
          {"role": "user", "content": f"주제가 들어갈 공간{prompt}"}
      ]
    )
    return response['choices'][0]['message']['content']

# Main page
def index(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            question= form['prompt'].value()
            message = generate_message(request, form['prompt'].value())
            context = {
              'question': question,
              'message': message,
            }
        return render(request, 'answer.html', context)
    else:
        form = AnswerForm()

    return render(request, "kist.html", {"form": form})