#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from cls import LocalFile, AmySQL

try:
    ii = 0
    data = AmySQL.get_table('select cid, md5 from zlib122 order by md5')
    dcount = len(data)
    for md5 in data:
        try:
            d4 = AmySQL.mysql_execute('insert into zlib121 (cid, md5) values (\'' + md5[0] + '\', \'' + md5[1] + '\')')
            ii = ii + 1
            print(str(ii) + '/' + str(dcount))
        except Exception as ex:
            print('\nMain-32-Exception:' + str(ex))
            LocalFile.write_LogFile('Main-Line-17-Exception:\n' + str(ex))# + '\r\nrecv_data:' + recv_data.decode('utf-8'))
        d4 = AmySQL.mysql_execute('delete from zlib122 where md5 = \'' + md5[0] + '\'')

    # i = 0
    # ii = 0
    # pagecount = 10000
    # while True:                     # 循环接受客户端的连接请求
    #     data = MySQL.get_table('select zlibrary_id, md5, md5_reported from books where zlibrary_id > ' + str(i * pagecount) + ' and zlibrary_id < ' + str((i + 1) * pagecount))
    #     for md5 in data:
    #         d3 = MySQL.mysql_execute('update zlib12 set md5 = \'' + md5[1] + '\' where zid = ' + str(md5[0]))
    #         d4 = MySQL.mysql_execute('update zlib121 set md5 = \'' + md5[2] + '\' where zid = ' + str(md5[0]))
    #         ii = ii + 1
    #         print(str(ii))
    #     i = i + 1
    #     print('R:' +str(i * pagecount))

    # while True:                     # 循环接受客户端的连接请求
        # data = MySQL.get_table('select zid from zlib12 where md5 is null limit 1000')
        # for j in data:
        #     # json_data.append(dict(zip(row_headers,result)))
        #     id = str(j[0])
        #     md5 = MySQL.get_table_one('select md5, md5_reported from books where zlibrary_id = ' + id)
        #     d3 = MySQL.mysql_execute('update zlib12 set md5 = \'' + md5[0] + '\' where zid = ' + id)
        #     d4 = MySQL.mysql_execute('update zlib121 set md5 = \'' + md5[1] + '\' where zid = ' + id)
except Exception as ex:
    print('\nMain-32-Exception:' + str(ex))
    LocalFile.write_LogFile('Main-Line-70-Exception:\n' + str(ex))# + '\r\nrecv_data:' + recv_data.decode('utf-8'))
            