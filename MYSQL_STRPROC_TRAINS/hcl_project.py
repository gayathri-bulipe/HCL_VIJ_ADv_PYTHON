from hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            self.cursor.callproc("get_no_avl_tkt")
            for r in self.cursor.stored_results():
                d=r.fetchone()
            return d
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def book(self):
        pass
b1=Booking()
b1.connect("localhost","root","Gayathri@123","traintickets")
sts=b1.available_seats()
print(sts)

seat_avl={}

seat_avl['train_no']=sts[0]
seat_avl['no_of_seats']=sts[1]
print(seat_avl)