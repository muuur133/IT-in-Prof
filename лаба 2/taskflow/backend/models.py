from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Project(db.Model):
   __tablename__ = "projects"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(120), nullable=False, unique=True)
   tasks = db.relationship("Task", back_populates="project")
class Task(db.Model):
   __tablename__ = "tasks"
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(200), nullable=False)
   status = db.Column(db.String(20), nullable=False, default="open")
   project_id = db.Column(
       db.Integer, db.ForeignKey("projects.id"), nullable=False
   )
   created_at = db.Column(db.DateTime, server_default=db.func.now())
   updated_at = db.Column(
      db.DateTime, server_default=db.func.now(), nullable=False
   )
   project = db.relationship("Project", back_populates="tasks")
   __table_args__ = (
      db.Index("idx_tasks_status", "status"),
      db.Index("idx_tasks_project", "project_id"),
   )