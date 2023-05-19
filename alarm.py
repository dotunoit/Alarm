{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a483833",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import winsound\n",
    "\n",
    "def set_alarm():\n",
    "    alarm_time = input(\"Enter the time of alarm to be set (in HH:MM format): \")\n",
    "    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))\n",
    "\n",
    "    while True:\n",
    "        current_time = time.localtime()\n",
    "        current_hour = current_time.tm_hour\n",
    "        current_minute = current_time.tm_min\n",
    "\n",
    "        if current_hour == alarm_hour and current_minute == alarm_minute:\n",
    "            print(\"Wake up!\")\n",
    "            # Play sound for 10 seconds\n",
    "            winsound.Beep(1000, 10000)\n",
    "            break\n",
    "\n",
    "        # Wait for 1 second before checking the time again\n",
    "        time.sleep(1)\n",
    "\n",
    "set_alarm()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fbcac4c4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
