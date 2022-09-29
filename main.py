# De TCP client
#
# Lees en knip de data op en stuur het naar de handler.
#
import etc.config as cfg
import soc_conn


if cfg.op_select == 1:
    import dbhandeling as func
else:
    import filehandeling as func



while True:


    # Pass the data to the handler
    func.passdata(soc_conn)

while False:
    s.close()
    print("Connection lost")
