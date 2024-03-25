"""As a strict big brother, I do limit my young brother Vasya on time he spends on computer games. I define a prime-time as a time period till which Vasya have a permission to play computer games. I specify start hour and end hour as pair of integers.

I need a function which will take three numbers - a present moment (current hour), a start hour of allowed time period and an end hour of allowed time period. The function should give answer to a question (as a boolean): "Can Vasya play in specified time?"

If I say that prime-time is from 12 till 15 that means that at 12:00 it's OK to play computer but at 15:00 there should be no more games.

I will allow Vasya to play at least one hour a day."""


def can_i_play(now_hour, start_hour, end_hour):
    if end_hour < start_hour and now_hour < start_hour:
        now_hour += 24
        end_hour += 24
    elif end_hour < start_hour and now_hour > start_hour or end_hour < start_hour and now_hour == start_hour:
        end_hour += 24
    return True if now_hour in range(start_hour, end_hour) else False
