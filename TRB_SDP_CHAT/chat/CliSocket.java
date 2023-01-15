import java.io.*;
import java.net.*;
import java.awt.*;

public class CliSocket extends Thread {
    InetAddress ER, IPr;
    DatagramSocket DS;
    byte bp[] = new byte[1024];
    TextArea ecran = new TextArea(10, 30);
    int port;
    int destPort;

    boolean regUser = false;
    boolean newPort = false;
    boolean confirm = false;

    CliSocket(TextArea ta) {
        ecran = ta;
    }

    public void setPort(int p){
        port = p;
    }

    public boolean getConfirm(){
        return confirm;
    }

    public void setConfirm(boolean c){
        confirm = c;
    }

    public int getdestPort(){
        return destPort;
    }

    public void setdestPort(int p){
        destPort = p;
    }

    public void receiveDP() {
        try {
            DatagramPacket DP = new DatagramPacket(bp, 1024);
            DS.receive(DP);
            IPr = DP.getAddress();
            byte Payload[] = DP.getData();
            int len = DP.getLength();
            String res = new String(Payload, 0, 0, len);

            //String tmp = IPr.toString();
            //String temp = tmp.substring(1);
            
            if (res.charAt(0) == '-' && res.charAt(1) == 'a'){
                destPort = Integer.parseInt(res.substring(2));
            }
            else{
                for (int i = 0; i < res.length(); i++){
                    if (res.charAt(i) == ','){
                        String temp = res.substring(2, i);
                        String capitalizeFirst = temp.substring(0, 1).toUpperCase() + temp.substring(1);
                        String newRes = res.substring(i + 1);
                        ecran.appendText("\n" + capitalizeFirst + ": " + newRes);
                        break;
                    }
                }
            }

        } catch (IOException e) {
        }
    }

    public void receiveRegDP(){
        try {
            DatagramPacket DP = new DatagramPacket(bp, 1024);
            DS.receive(DP);
            IPr = DP.getAddress();
            byte Payload[] = DP.getData();
            int len = DP.getLength();
            String res = new String(Payload, 0, 0, len);

            if (res.charAt(0) == 'y'){
                confirm = true;
            }

            if (res.charAt(0) == 'p'){
                String tmp = res.substring(1);
                int p = Integer.parseInt(tmp);
                setPort(p);
                regUser = true;
                newPort = true;
            }

        } catch (IOException e) {
        }
    }

    public void sendDP(int Pr, String msg, String end) {
        int len = msg.length();
        byte b[] = new byte[len];
        msg.getBytes(0, len, b, 0);
        try {
            ER = InetAddress.getByName(end);
            DatagramPacket DP = new DatagramPacket(b, len, ER, Pr);
            DS.send(DP);
        } catch (IOException e) {
        }
    }

    public void sendtoServices(int Pr, String msg) {
        int len = msg.length();
        byte b[] = new byte[len];
        msg.getBytes(0, len, b, 0);
        try {
            ER = InetAddress.getByName("127.0.0.1");
            DatagramPacket DP = new DatagramPacket(b, len, ER, Pr);
            DS.send(DP);
        } catch (IOException e) {
        }
    }

    public void run() {
        try {
            DS = new DatagramSocket();
            System.out.println("Porta: " + DS.getLocalPort());
        } catch (IOException e) {
        }
        while (!regUser && !newPort){
            receiveRegDP();
        }
        DS.close();
        try {
            DS = new DatagramSocket(port);
            System.out.println("Nova porta: " + DS.getLocalPort());
            
        } catch (IOException e) {
        }
        while (true){
            receiveDP();
        }
    }
}