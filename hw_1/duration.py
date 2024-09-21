def cal_dur(duration):
    if duration < 60:
        s_duration = duration
        print(f'{s_duration} сек')
    elif duration < 3600:
        m_duration = duration//60
        s_duration = duration%60
        print(f'{m_duration} мин {s_duration} сек')
    elif duration < 86400:
        h_duration = duration // 3600
        m_duration = (duration % 3600)//60
        s_duration = duration % 60
        print(f'{h_duration} час {m_duration} мин {s_duration} сек')
    else:
        d_duration = duration // 86400
        h_duration = (duration % 86400)//3600
        m_duration = (duration % 3600) // 60
        s_duration = duration % 60
        print(f'{d_duration} дн {h_duration} час {m_duration} мин {s_duration} сек')

while True:
    duration = int(input('Продолжительность конвертировать секунды: '))
    if duration == 0:
        break
    else:
        cal_dur(duration)

