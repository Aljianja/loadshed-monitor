Certainly! Here's a sample documentation on how to use the Python script:

## Loadshed Monitor Script Documentation

The Loadshed Monitor script is a Python script that allows you to monitor the power status of your computer and receive email notifications when the power is restored or disconnected due to loadshedding. The script periodically checks the power status and sends email notifications accordingly.

### Prerequisites

Before using the Loadshed Monitor script, ensure that you have the following:

1. Python: Make sure Python is installed on your system. You can download Python from the official website: [python.org](https://www.python.org/downloads/)

2. Required Python Packages: Install the necessary Python packages by running the following command in your terminal or command prompt:
   ```
   pip install psutil python-dotenv
   ```

3. SMTP Server Details: Obtain the SMTP server details (server address, port number, username, password) for sending emails. You can use popular email providers like Gmail or consult your email service provider for the SMTP server details.

### Setup

1. Clone or download the Loadshed Monitor script to your local machine.

2. Create an `.env` file in the same directory as the script. Open the `.env` file in a text editor and provide the following information:

   ```
   SMTP_SERVER=your_smtp_server
   SMTP_PORT=your_smtp_port
   SMTP_USERNAME=your_email_username
   SMTP_PASSWORD=your_email_password
   FROM_ADDRESS=your_email_address
   TO_ADDRESS=recipient_email_address
   ```

   Replace the placeholders (`your_smtp_server`, `your_smtp_port`, `your_email_username`, `your_email_password`, `your_email_address`, `recipient_email_address`) with the corresponding values.

### Usage

1. Open a terminal or command prompt and navigate to the directory where the Loadshed Monitor script is located.

2. Run the following command to start the script:
   ```
   python loadshed_monitoring.py
   ```

3. The script will start monitoring the power status of your computer.

4. When the power status changes (AC power plugged in or running on battery), the script will send an email notification to the specified recipient email address.

5. To stop the script, press `Ctrl+C` in the terminal or command prompt.

### Customization

The Loadshed Monitor script can be customized to fit your specific requirements. Here are some possible customizations:

- **Notification Message:** Modify the content of the email notification messages in the `send_email` function within the script. You can include additional details or customize the message format according to your preferences.

- **Monitoring Interval:** By default, the script checks the power status every 60 seconds. If you want to change the monitoring interval, modify the `time.sleep(60)` line within the `main` function. Adjust the value to the desired number of seconds.

### Troubleshooting

- If you encounter any errors or issues while running the script, ensure that all the prerequisites are met, including the installation of required Python packages and providing correct SMTP server details in the `.env` file.

- Check the console output for any error messages or exceptions raised by the script. These messages can help identify the cause of the problem.

- Make sure the recipient email address specified in the `.env` file is correct and can receive emails.

### Conclusion

The Loadshed Monitor script provides a convenient way to monitor the power status of your computer and receive email notifications when the power is restored or disconnected due to loadshedding. By following the setup instructions and running the script, you can stay informed about power fluctuations and take necessary actions accordingly.

Note: The script is provided as-is and may require modifications to fit specific use cases or operating environments.