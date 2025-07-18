weekly_calendar: dict[str, bool] = {'Monday': True, 'Tuesday': False, 'Wednesday': True, 'Thursday': False, 'Friday': True, 'Saturday': False, 'Sunday': False}
available_days = []

for day, availability in weekly_calendar.items():
    if availability == True:
        available_days += [day]

print(f'Total available days: {len(available_days)}')
print(available_days)