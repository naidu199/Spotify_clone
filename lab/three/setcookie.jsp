
<%
String uname=request.getParameter("username");
Cookie ck = new Cookie ("username",uname);
ck.setMaxAge(1* 60);
response.addCookie(ck);
%>
<html>
<body>
<h3>Cookie Saved</h3>
<p><a href="showcookie.jsp">View the cookie value</a><p>
</body>
</html>
