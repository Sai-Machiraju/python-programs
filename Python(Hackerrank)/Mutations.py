def mutate_string(str, p, ch):
    l=list(str)
    l[p]=ch
    str="".join(l)
    return str

