# Reminders Module
import json
import schedule
import time
from datetime import datetime, timedelta
import threading
import config

class ReminderManager:
    def __init__(self):
        self.reminders = []
        self.reminder_thread = None
        self.running = False
        self.load_reminders()
    
    def load_reminders(self):
        """Load reminders from file"""
        try:
            with open(config.REMINDER_STORAGE_FILE, 'r') as f:
                self.reminders = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.reminders = []
    
    def save_reminders(self):
        """Save reminders to file"""
        try:
            with open(config.REMINDER_STORAGE_FILE, 'w') as f:
                json.dump(self.reminders, f, indent=2)
        except Exception as e:
            print(f"Error saving reminders: {e}")
    
    def add_reminder(self, message, delay_minutes):
        """Add a reminder"""
        reminder = {
            'id': len(self.reminders) + 1,
            'message': message,
            'created_at': datetime.now().isoformat(),
            'trigger_at': (datetime.now() + timedelta(minutes=delay_minutes)).isoformat(),
            'triggered': False
        }
        
        self.reminders.append(reminder)
        self.save_reminders()
        
        # Schedule the reminder
        schedule.every(delay_minutes).minutes.do(self.trigger_reminder, reminder['id'])
        
        return f"Reminder set: '{message}' in {delay_minutes} minutes"
    
    def trigger_reminder(self, reminder_id):
        """Trigger a reminder"""
        for reminder in self.reminders:
            if reminder['id'] == reminder_id and not reminder['triggered']:
                reminder['triggered'] = True
                self.save_reminders()
                return f"Reminder: {reminder['message']}"
        return ""
    
    def list_reminders(self):
        """List all active reminders"""
        active = [r for r in self.reminders if not r['triggered']]
        if not active:
            return "No active reminders"
        
        result = "Active reminders:\n"
        for r in active:
            trigger_time = datetime.fromisoformat(r['trigger_at'])
            result += f"- {r['message']} (at {trigger_time.strftime('%H:%M')})\n"
        return result
    
    def delete_reminder(self, reminder_id):
        """Delete a reminder"""
        for i, r in enumerate(self.reminders):
            if r['id'] == reminder_id:
                del self.reminders[i]
                self.save_reminders()
                return f"Reminder {reminder_id} deleted"
        return f"Reminder {reminder_id} not found"
    
    def start_scheduler(self):
        """Start the reminder scheduler in background"""
        if not self.running:
            self.running = True
            self.reminder_thread = threading.Thread(target=self._run_scheduler, daemon=True)
            self.reminder_thread.start()
    
    def _run_scheduler(self):
        """Run the scheduler loop"""
        while self.running:
            schedule.run_pending()
            time.sleep(1)
    
    def stop_scheduler(self):
        """Stop the reminder scheduler"""
        self.running = False
        if self.reminder_thread:
            self.reminder_thread.join(timeout=1)
