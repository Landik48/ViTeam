import xlrd, sqlite3

connect = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = connect.cursor()

def excel_pers(perspath):
    cursor.execute("DELETE FROM main_users")
    connect.commit()
    excel_pers = xlrd.open_workbook(perspath).sheet_by_index(0)
    for x in range(excel_pers.nrows):
        lst = list()
        for y in range(4):
            el = excel_pers.cell_value(x, y)
            lst.append(el)
        cursor.execute("""INSERT INTO  
    main_users(name, team, theme, scores_personal)
    VALUES(?,?,?,?)""", (lst[0], lst[1], lst[3], lst[2]))
    connect.commit()

def excel_team(teampath):
    cursor.execute("DELETE FROM main_teams")
    connect.commit()
    excel_team = xlrd.open_workbook(teampath).sheet_by_index(0)
    for x in range(excel_team.nrows):
        lst = list()
        for y in range(2):
            el = excel_team.cell_value(x, y)
            lst.append(el)
        cursor.execute("""INSERT INTO  
    main_teams(team, scores_team)
    VALUES(?,?)""", (lst[0], lst[1]))
    connect.commit()