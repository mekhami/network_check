import subprocess
import sys
import time


def pingtest():
    num_success = 0
    num_fails = 0
    avg_ping = 0
    max_ping = 0
    num_high_pings = 0

    ping_list = []
    
    while True:
        p = subprocess.Popen(['ping', 'google.com', '-c1', '-n', '-W3'], stdout=subprocess.PIPE)
        output = p.communicate()[0]

        if output == '' and p.poll() is not None:
            pass
        elif output != '':
            if len(output) == 167:
                num_fails += 1
            else:
                num_success += 1
                result = output.split()[13]
                pingtime = float(result[5:])
                ping_list.append(pingtime)
                avg_ping = round((sum(ping_list)/len(ping_list)), 2)
                max_ping = max(ping_list)
                num_high_pings = len([i for i in ping_list if i > 500])

        else:
            print 'Something went wrong.'

        temp = "Successes: {0} - Fails: {1} - Average of Successful Pings - {2} - Max Ping - {3} - Number of High Pings - {4}"
        print temp.format(num_success, num_fails, avg_ping, max_ping, num_high_pings)

        time.sleep(5)

if __name__ == '__main__':
    pingtest()
		
