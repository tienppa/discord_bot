# discord_bot

Welcome to the repository for My Discord Bot! This bot is designed to enhance your Discord server with features like:  
Greetings: Welcomes new members with a friendly message.  
Birthday Wishes: Celebrates members' birthdays.  
Inspirational Quotes: Provides daily quotes with beautiful images to inspire and motivate.  
Scheduled Tasks: Wakes up the server with a cheerful message at a set time.  
![Image Alt Text](https://github.com/tienppa/discord_bot/assets/170253215/ad63a5f1-d01d-4087-be67-f2e1537440a4)

## Installation
```base
# SSH into your server: 
ssh your_username@your_server_ip

# Clone the Repository:
git clone https://github.com/your-username/your-repository.git

# Create Virtual Environment
Navigate to your bot's directory: cd /home/your_username/my_discord_bot
Activate the virtual environment: source my_bot_env/bin/activate

# Install Dependencies:
pip install -r requirements.txt

# Create User:
sudo adduser botuser

# Grant Permissions:
sudo usermod -aG sudo botuser
sudo chown -R botuser:botuser /home/code/discord_bot

# Reload the systemd daemon: 
sudo systemctl daemon-reload

# Restart the service: 
sudo systemctl restart discord-bot.service

# Check the status: 
sudo systemctl status discord-bot.service

# Examine System Logs: 
journalctl -u discord-bot.service
```



