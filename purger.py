import discord
import asyncio  # Use asyncio.sleep instead of time.sleep

def main():
    # Display the instructions
    print("""
Instructions:
1. Enter "1" to delete direct messages with a user.
2. Enter "2" to delete messages in a channel.
    """)

    while True:
        # Get the user's input
        PURGER_OPTION = input("Enter your option (1 or 2): ").strip()

        # Execute code based on user input
        if PURGER_OPTION == "1":
            run_directmessage_purger()
            break
        elif PURGER_OPTION == "2":
            run_channelmessage_purger()
            break
        else:
            print("Wrong input. Please enter 1 or 2.")

def run_directmessage_purger():
    # Code to run if the option is "1"
    print("Executing the direct message purger...")

    # Get Discord token and user ID from the user
    TOKEN = input('Enter your Discord token: ')  
    RECIPIENT_USER_ID = input('Enter the user ID: ')

    # Define the client class
    class MyClient(discord.Client):
        async def on_ready(self):
            print(f'Logged on as {self.user}!')

            user = await self.fetch_user(int(RECIPIENT_USER_ID))
            if user:
                dm_channel = await user.create_dm()
                async for message in dm_channel.history(limit=100000):
                    if message.author == self.user and (message.type == discord.MessageType.default or message.type == discord.MessageType.reply):
                        try:
                            await message.delete()
                            print(f'Deleted message: {message.content}')
                            await asyncio.sleep(2)
                        except discord.Forbidden:
                            print("Lacked permissions to delete a message.")
                        except discord.HTTPException as e:
                            print(f"Failed to delete message: {e}")
                print("Completed deleting messages.")
            else:
                print("User not found.")

            await self.close()

    # Create an instance of the client and run it
    client = MyClient()
    client.run(TOKEN)

def run_channelmessage_purger():
    # Code to run if the option is "2"
    print("Executing the channel message purger...")

    # Get Discord token and channel ID from the user
    TOKEN = input('Enter your Discord token: ')  
    CHANNEL_ID = input('Enter the channel ID: ')

    # Define the client class
    class MyClient(discord.Client):
        async def on_ready(self):
            print(f'Logged on as {self.user}!')

            channel = await self.fetch_channel(int(CHANNEL_ID))
            if channel:
                async for message in channel.history(limit=100000):
                    if message.author == self.user and (message.type == discord.MessageType.default or message.type == discord.MessageType.reply):
                        try:
                            await message.delete()
                            print(f'Deleted message: {message.content}')
                            await asyncio.sleep(2)
                        except discord.Forbidden:
                            print("Lacked permissions to delete a message.")
                        except discord.HTTPException as e:
                            print(f"Failed to delete message: {e}")
                print("Completed deleting messages.")
            else:
                print("Channel not found.")

            await self.close()

    # Create an instance of the client and run it
    client = MyClient()
    client.run(TOKEN)

async def purge_messages(channel):
    # Helper function to purge messages
    async for message in channel.history(limit=100000):
        if message.author == channel.guild.me and (message.type == discord.MessageType.default or message.type == discord.MessageType.reply):
            try:
                await message.delete()
                print(f'Deleted message: {message.content}')
                await asyncio.sleep(2)  # Be cautious with the sleep time
            except discord.Forbidden:
                print("Lacked permissions to delete a message.")
            except discord.HTTPException as e:
                print(f"Failed to delete message: {e}")
    print("Completed deleting messages.")

# Ensure that the main function is called when the script is executed
if __name__ == "__main__":
    main()