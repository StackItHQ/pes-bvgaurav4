from pyngrok import ngrok


public_url = ngrok.connect(5000).public_url

print(public_url)

ngrok_process = ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print(" Shutting down server.")
    ngrok.kill()