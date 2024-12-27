# Solution shamelessly stolen from: https://topaz.github.io/paste/#XQAAAQDAAQAAAAAAAAAzHIoib6poHLpewxtGE3pTrRdzrponKxDhfDpmqUbmwC6eNytFiAtpkMiCqeghNLV2zaw8KSdzSEgXG3fzAq9S86ZmDlpLKRv41QjaGoPMIOjliWR5SLyfp1w/AAVy/FzxwYh6hhYb8UqJYJH75Rz/cc8aK+sCP/lFJwcsXr124+25Uaasqd4vs7FGUGyyagyZ+JDL4iM9ivvgbtVIFkoRRNt583UCDIN1BOtDZG8xZmrmdt77IqHBrIqN+4+qo2Ju43pDk/eukPUU+WMG1AluFJzBpCioq7ZG6s8nyVhCUxzPWdQ5V98X3+VKzUkz/QC1aEpPZTeGPR725wr0PRLVKq6XH/Ld4D/NDOVutTbAVC0lF+yrkOUQ1mqw7EQ2PsqGertTc1QLKEO0SPwfrB11LnQK4f+B83UA
from functools import cache


def path(ss):
    (y, x), (Y, X) = [divmod('789456123_0A<v>'.find(t), 3) for t in ss]
    S = '>' * (X - x) + 'v' * (Y - y) + '0' * (y - Y) + '<' * (x - X)
    return S if (3, 0) in [(y, X), (Y, x)] else S[::-1]


@cache
def length(S, d):
    if d < 0:
        return len(S) + 1
    return sum(length(path(ss), d - 1) for ss in zip('A' + S, S + 'A'))


for r in 2, 25:
    print(sum(int(S[:3]) * length(S[:3], r) for S in open('21_input.txt')))
