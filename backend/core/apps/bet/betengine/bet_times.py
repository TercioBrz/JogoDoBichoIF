from datetime import datetime , timedelta

def rodada_atual():

    agora = datetime.now()

    if agora.minute < 30:
        return agora.replace(minute=0,second=0,microsecond=0)

    return agora.replace(minute=30,second=0,microsecond=0)


def rodada_fechada():
    agora = datetime.now()

    if agora.minute < 30:
        base = agora.replace(minute=0,second=0,microsecond=0)
        return base - timedelta(minutes=30)

    return agora.replace(minute=30,second=0,microsecond=0)

        