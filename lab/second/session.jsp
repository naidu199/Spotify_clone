<html>
<body>
<%
String name=request.getParameter("uname");
out.print("Welcome "+name);
session.setAttribute("user",name);
%>
<br/>
<a href="second.jsp">Next Page</a>
</body>
</html>
