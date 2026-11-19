from app import app
from models import Project, Task, db

with app.app_context():
  if Task.query.count() == 0:
     study = Project(name="Учебный проект")
     personal = Project(name="Личные задачи")
     db.session.add_all([study, personal])
     db.session.flush()
     
     db.session.add_all([
        Task(title="Создать базу данных", status="done",
           project_id=study.id),
        Task(title="Добавить модели", status="in_progress",
           project_id=study.id),
        Task(title="Проверить GET /tasks", status="open",
           project_id=study.id),
        Task(title="Подготовить отчёт", status="open",
           project_id=personal.id),
        Task(title="Ответить на вопросы", status="open",
           project_id=personal.id),
     ])
     db.session.commit()
     print("Создано 5 задач")
  else:
     print("Seed пропущен: задачи уже существуют")