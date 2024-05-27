from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import time
import requests

def schedule_telegram_task(bot, token, chat_id):
    scheduler = AsyncIOScheduler()

    async def send_notification():
        # Get current time in DD/MM/YYYY HH:MM format
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        message = f"2Tien: {current_time}"

        # Generate random image URL with epoch time
        image_url = f"https://picsum.photos/500/150?random={int(time.time())}"

        # Send notification
        api_url = f"https://api.telegram.org/bot{token}/sendPhoto"
        data = {
            'chat_id': chat_id,
            'caption': message
        }

        files = {
            'photo': (image_url, requests.get(image_url).content)
        }

        requests.post(api_url, data=data, files=files)

    scheduler.add_job(send_notification, 'cron', minute='0') 
    scheduler.start()

