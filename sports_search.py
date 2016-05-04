import psycopg2
import os
import sys
conn = psycopg2.connect("dbname=Pipita user=Pipita host=/tmp/")
cur = conn.cursor()




#-----------------------------------------------

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

#-------------------------------------------

def catch_invalid_input(user_input_1, user_input_2):

    if user_input_1 != 0:
        if not user_input_1.isdigit() or int(user_input_1) > 4:
            input("Invalid input. Press enter to continue!... " )
            return True
        else:
            return False

    if user_input_2.isdigit():
        return user_input_2
    else:
        print('\n')
        input('Invalid entry..!!')
        return False



#-----------------------------

#-----------------------------------------------------------

def get_menu_choices(choice):

    if catch_invalid_input(choice, 0):
        return 0


    elif int(choice) == 1:
        cur.execute("SELECT * FROM sports_stats_tbl;")
        column_names = [desc[0] for desc in cur.description]
        # cur.execute("DECLARE julio SCROLL CURSOR FOR SELECT * FROM sports_stats_tbl;")
        # cur.execute('FETCH FORWARD 5 FROM julio;')
        # print(column_names)
        # input()
        dis_row = 20
        dis_col = 35
        for _ in column_names:

            if dis_col == 35:
                print_there(18, dis_col, _)
                dis_col += 5

            elif dis_col == 40:
                print_there(18, dis_col, _)
                dis_col += 12

            else:
                print_there(18, dis_col, _)
                dis_col += 7

        print_there(19,35, "---------------------------------------------------------------------------")
        for record in cur:
            print_there(dis_row,35, record)
            dis_row += 1
            #print(record)
        input()
        return 0
    #
    # elif int(choice) == 2:
    #

    #
    elif int(choice) == 3:

        cur.execute("COPY sports_stats_tbl(id, player_name, ru_att, ru_yds, ru_avg, ru_td, re_rec, re_yds, re_avg, re_td) FROM '/Users/Pipita/Sports_Search_Engine/sports_stats.csv' DELIMITER',' CSV")
        conn.commit()
        return 0




#-----------------------------------------------------------

def main():

    while True:

        os.system('clear')
        print('WELCOME TO FOOTBALL RUSH & RECEIVE STATS')
        print('\n\n')
        print('MAIN MENU:\n')
        print('1.) See Data Base content \n')
        print('2.) Insert new data\n')
        print('3.) Insert a sample of data into Data Base \n')
        print('4.) Quit Program\n\n\n')

        user_menu_choice = input("Choose a number option and press enter: ")

        if catch_invalid_input(user_menu_choice,0):
            continue
        else:
            if get_menu_choices(user_menu_choice) == 0:
                continue
            else:
                print('\n\n')
                print("Bye... Have a Nice Day!")
                print('\n\n')
                sys.exit()




if __name__ == '__main__':
    main()
