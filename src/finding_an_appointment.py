"""
The businesspeople among you will know that it's often not easy to find an appointment. In this kata we want to find
such an appointment automatically. You will be given the calendars of our businessperson and a duration for the meeting.
Your task is to find the earliest time, when every businessperson is free for at least that duration.

Example Schedule:

Person | Meetings
-------+-----------------------------------------------------------
     A | 09:00 - 11:30, 13:30 - 16:00, 16:00 - 17:30, 17:45 - 19:00
     B | 09:15 - 12:00, 14:00 - 16:30, 17:00 - 17:30
     C | 11:30 - 12:15, 15:00 - 16:30, 17:45 - 19:00
Rules:

All times in the calendars will be given in 24h format "hh:mm", the result must also be in that format
A meeting is represented by its start time (inclusively) and end time (exclusively) -> if a meeting takes place from
09:00 - 11:00, the next possible start time would be 11:00
The businesspeople work from 09:00 (inclusively) - 19:00 (exclusively), the appointment must start and end within
that range
If the meeting does not fit into the schedules, return null or None as result
The duration of the meeting will be provided as an integer in minutes
Following these rules and looking at the example above the earliest time for a 60 minutes meeting would be 12:15.

Data Format:

The schedule will be provided as 3-dimensional array. The schedule above would be encoded this way:

[
  [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]
[ [("09:00", "11:30"), ("13:30", "16:00"), ("16:00", "17:30"), ("17:45", "19:00")]
, [("09:15", "12:00"), ("14:00", "16:30"), ("17:00", "17:30")]
, [("11:30", "12:15"), ("15:00", "16:30"), ("17:45", "19:00")]
]
"""


def get_start_time(schedules, duration):
    _min = 9 * 60
    _max = 19 * 60
    available = []
    for sch in schedules:
        _sch = []
        last = _min
        for sc in sch:
            _from = timestr_to_minutes(sc[0])
            if last + duration <= _from:
                _sch.append([last, _from])
            last = timestr_to_minutes(sc[1])
        if last + duration <= _max:
            _sch.append([last, _max])
        available.append(_sch)

    print(available)


def timestr_to_minutes(timestr):
    splitime = timestr.split(':')
    return int(splitime[0]) * 60 + int(splitime[1])


def minutes_to_timestr(minutes):
    return '{}:{}'.format(minutes // 60, minutes % 60)
