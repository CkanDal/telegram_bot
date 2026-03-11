import subprocess 

def get_speed() -> str:
    result = subprocess.run(["sar", "-n", "DEV", "1", "1"], 
    capture_output=True, text=True)

    for line in result.stdout.splitlines():
        parts = line.split()
        if parts and parts[0] != 'Average:' and parts[1] == 'ens3':
            rx = parts[4]
            tx = parts[5]

            return f"RX {rx} kB/s | TX {tx} kB/s"
        
        

