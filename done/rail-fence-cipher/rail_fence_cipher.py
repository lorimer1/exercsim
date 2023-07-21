def rail_index_generator(rails: int) -> int:
    current_value = 0
    incrementing = True

    while True:
        yield current_value

        if incrementing:
            current_value += 1
            if current_value == rails - 1:
                incrementing = False
        else:
            current_value -= 1
            if current_value == 0:
                incrementing = True


def encode(message:str, rails:int):
    message = [c for c in message]
    result_List = ["" for _ in range(rails)]
    rail_index = rail_index_generator(rails)

    while( message ):
        char = message.pop(0)
        result_List[next(rail_index)] += char

    return ''.join(result_List)

def decode(encoded_message:str, rails:int):
    # get number of chars per rail index
    rail_char_counts = [0 for _ in range(rails)]
    rail_index = rail_index_generator(rails)
    for _ in encoded_message:
        rail_char_counts[next(rail_index)] += 1

    # get chars for each rail
    rail_chars = list()
    pos = 0
    for i in range(rails):
        rail_chars.append( [char for char in encoded_message[pos : pos + rail_char_counts[i]]] )
        pos += rail_char_counts[i]

    # decode
    result = ""
    rail_index = rail_index_generator(rails)
    for _ in encoded_message:
        result += rail_chars[next(rail_index)].pop(0)

    return result

if __name__ == "__main__":
    print(decode("WECRLTEERDSOEEFEAOCAIVDEN", 3))