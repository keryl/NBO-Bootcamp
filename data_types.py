def data_type(m):
    """ Takes an input and returns the corresponding value"""
    m_type = type(m)
    if m_type == str:
        return len(m)
    elif m_type == bool:
        return m
    elif m_type == int:
        if m < 100:
            return "less than 100"
        elif m_type == 100:
            return "equal to 100"
        else:
            return "more than 100"
    elif m_type == list:
        if len(m) >= 3: # length should be equal or greater than 3 in order to access the 3rd item
          return m[2]
        else:
          return None
    else:
        return "no value"
