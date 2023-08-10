import os
if __name__=="__main__":

    print("Welcome")
    while(True):
        s=input("Saysss it: ")
        if(s=="q"):
            print("thanks");
            break
        command=f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{s}');"
        os.system(command)
     
