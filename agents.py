from datetime import datetime
import os

class AIAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.history = []

    def execute_task(self, task, files=[]):
        # نموذج تنفيذ المهمة مع دعم الملفات
        result = f"{self.name} نفذ المهمة: {task} مع {len(files)} ملفات."
        self.history.append({
            "task": task,
            "files": [f.filename for f in files],
            "result": result,
            "timestamp": datetime.now().isoformat()
        })
        return result

class ChiefAI:
    def __init__(self):
        self.agents = {
            "marketing": AIAgent("MarketingAgent", "جدب المطاعم و السائقين"),
            "developer": AIAgent("DeveloperAgent", "بناء و تنظيم الأكواد"),
            "support": AIAgent("SupportAgent", "الرد على الرسائل و النزاعات"),
            "director": AIAgent("DirectorAgent", "مراقبة نظام الطلبات بالكامل"),
            "comptable": AIAgent("ComptableAgent", "مراقبة الأرباح و الميزانية"),
            "advisor": AIAgent("AdvisorAgent", "اقتراحات التحسين و النمو")
        }

    def delegate(self, agent_name, task, files=[]):
        agent = self.agents.get(agent_name)
        if not agent:
            return f"Agent '{agent_name}' غير موجود"
        return agent.execute_task(task, files)
