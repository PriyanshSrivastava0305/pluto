import openai
from flask import Flask, render_template,request


class Person:
  
    openai.api_key="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"


    app = Flask(__name__)
    @app.route('/',methods=['POST','GET'])

    def myfunc():
        # print(self.reply_content)
        if request.method=='POST':
            prompt = request.form.get("prompt")
            print(prompt)
            completion=openai.ChatCompletion.create(    
                model="gpt-3.5-turbo",
                messages=[{"role": "user","content": "only and only reply in hinglish and in a sercastic way do not use english at all "+prompt}]
            )
            reply=completion.choices[0].message.content
            print("pluto")
            print(reply)
            return render_template('index.html',reply=reply)
        
        return render_template('index.html')

    # def main():
    
    #     user_input = input(f"Enter msg : {user_input}")
    #     completion=openai.ChatCompletion.create(    
    #         model="gpt-3.5-turbo",
    #         messages=[{"role": "user","content": "only and only reply in hinglish and in a sercastic way do not use english at all "+user_input}]
    #     )
    #     reply=completion.choices[0].message.content
    #     print
    #     return render_template('index.html',reply=reply)
    #     # return reply_content

    if __name__ == '__main__':
        app.run(debug=True)


# while True:
#     p1 = Person("")
#     p1.myfunc()

