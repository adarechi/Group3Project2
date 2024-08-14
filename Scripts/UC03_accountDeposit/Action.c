Action()
{

	web_add_auto_header("Priority", 
		"u=0, i");

	web_revert_auto_header("Priority");

	web_add_auto_header("DNT", 
		"1");

	web_add_auto_header("Sec-GPC", 
		"1");

	web_add_header("Upgrade-Insecure-Requests", 
		"1");

	web_url("77.50.236.214:42030", 
		"URL=http://77.50.236.214:42030/", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t1.inf", 
		"Mode=HTML", 
		EXTRARES, 
		"Url=/static/js/2.7c253607.chunk.js", ENDITEM, 
		"Url=/logo192.png", ENDITEM, 
		LAST);

	web_set_sockets_option("SSL_VERSION", "AUTO");

	web_add_header("Access-Control-Request-Method", 
		"GET");

	web_add_header("Access-Control-Request-Headers", 
		"authorization");

	web_add_auto_header("Origin", 
		"http://77.50.236.214:42030");

	web_add_auto_header("Priority", 
		"u=4");

	web_custom_request("bank.wsdl", 
		"URL=http://77.50.236.203:4879/ws/bank.wsdl", 
		"Method=OPTIONS", 
		"TargetFrame=", 
		"Resource=1", 
		"Referer=http://77.50.236.214:42030/", 
		"Snapshot=t2.inf", 
		LAST);

	/*web_websocket_send("ID=1", 
		"Buffer={\"messageType\":\"hello\",\"broadcasts\":{\"remote-settings/monitor_changes\":\"\\\"1723531614118\\\"\"},\"use_webpush\":true}", 
		"IsBinary=0", 
		LAST);             */

	/*Connection ID 1 received buffer WebSocketReceive0*/

	lr_start_transaction("UC03_T01_userLogin");

	web_add_header("Access-Control-Request-Headers", 
		"content-type");

	web_add_header("Access-Control-Request-Method", 
		"POST");

	lr_think_time(114);

	web_custom_request("login", 
		"URL=http://77.50.236.203:4879/login", 
		"Method=OPTIONS", 
		"TargetFrame=", 
		"Resource=0", 
		"Referer=http://77.50.236.214:42030/", 
		"Snapshot=t3.inf", 
		"Mode=HTML", 
		LAST);

	web_add_auto_header("Priority", 
		"u=0");

	web_reg_save_param("accessToken",
		"LB=\"access_token\":\"",
		"RB=\"",
		LAST);
	
	web_custom_request("login_2", 
		"URL=http://77.50.236.203:4879/login", 
		"Method=POST", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=application/json", 
		"Referer=http://77.50.236.214:42030/", 
		"Snapshot=t4.inf", 
		"Mode=HTML", 
		"EncType=application/json", 
		"Body={\"username\":\"admin@pflb.ru\",\"password\":\"admin\"}", 
		LAST);

	web_add_cookie("jwt={accessToken}; DOMAIN=77.50.236.214");

	web_revert_auto_header("Origin");

	web_add_auto_header("Priority", 
		"u=0, i");

	web_revert_auto_header("Priority");

	web_add_header("Upgrade-Insecure-Requests", 
		"1");

	web_url("77.50.236.214:42030_2", 
		"URL=http://77.50.236.214:42030/", 
		"TargetFrame=", 
		"Resource=0", 
		"Referer=", 
		"Snapshot=t5.inf", 
		"Mode=HTML", 
		EXTRARES, 
		"Url=/static/js/2.7c253607.chunk.js", ENDITEM, 
		LAST);

	web_add_auto_header("Origin", 
		"http://77.50.236.214:42030");

	web_url("bank.wsdl_2", 
		"URL=http://77.50.236.203:4879/ws/bank.wsdl", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/xml", 
		"Referer=http://77.50.236.214:42030/", 
		"Snapshot=t6.inf", 
		"Mode=HTML", 
		LAST);

	lr_end_transaction("UC03_T01_userLogin",LR_AUTO);

	lr_start_transaction("UC03_T02_accountDeposit");

	web_add_header("Priority", 
		"u=4");

	web_add_header("Access-Control-Request-Headers", 
		"authorization");

	web_add_header("Access-Control-Request-Method", 
		"POST");

	lr_think_time(53);

	web_custom_request("1000", 
		"URL=http://77.50.236.203:4879/user/{userId}/money/{deposit}", 
		"Method=OPTIONS", 
		"TargetFrame=", 
		"Resource=0", 
		"Referer=http://77.50.236.214:42030/", 
		"Snapshot=t7.inf", 
		"Mode=HTML", 
		LAST);

	web_add_header("Priority", 
		"u=0");

	web_add_header("Authorization", 
		"Bearer {accessToken}");
	
	web_custom_request("1000_2", 
		"URL=http://77.50.236.203:4879/user/{userId}/money/{deposit}", 
		"Method=POST", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=application/json", 
		"Referer=http://77.50.236.214:42030/", 
		"Snapshot=t8.inf", 
		"Mode=HTML", 
		"EncType=", 
		LAST);

	lr_end_transaction("UC03_T02_accountDeposit",LR_AUTO);

	return 0;
}