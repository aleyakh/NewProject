from functions import get_all, get_by_pk, get_by_skill
from flask import Flask

def main():
    app = Flask(__name__)

    @app.route('/')
    def page_index():
        candidates = get_all()  # Возвращает всех кандидатов одним списком
        result = ""
        for candi in candidates:
            result = result + (f"Имя кандидата - {candi[0]}<br>Позиция кандидата - {candi[1]}<br>Навыки - {candi[2]}<br><br>")
        return f"<pre>\n{result}</pre>"

    @app.route('/candidates/<int:pk>')
    def page_candidates(pk):
        candidates_pk = get_by_pk(pk)  # Возвращает кандидата по Pk
        return f"<img src='{candidates_pk['picture']}'><br>" \
               f"<pre>" \
               f"Имя кандидата - {candidates_pk['name']}<br>" \
               f"Позиция кандидата - {candidates_pk['position']}<br>" \
               f"Навыки - {candidates_pk['skills']}" \
               f"</pre>"

    @app.route('/skills/<sk>')
    def page_skills(sk):
        candidates_skill = get_by_skill(sk) #Возвращает кандидатов по Skills
        result = ""
        for skill in candidates_skill:
            result = result + (f"Имя кандидата - {skill[0]}<br>Позиция кандидата - {skill[1]}<br>Навыки - {skill[2]}<br><br>")
        return f"<pre>\n{result}</pre>"

    app.run()

if __name__ == "__main__":
    main()
