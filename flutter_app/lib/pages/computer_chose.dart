// ignore_for_file: prefer_const_constructors

import 'dart:collection';
import 'dart:convert';
import 'dart:developer';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app/information.dart';
import 'package:http/http.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../input_validator.dart';
import 'control_page.dart';
import 'login_page.dart';

// void main() => runApp(MyApp());
//
// class MyApp extends StatefulWidget {
//   @override
//   State<MyApp> createState() => _MyAppState();
// }
//
// class _MyAppState extends State<MyApp> {
//   @override
//   Widget build(BuildContext context) {
//     return const MaterialApp(title: 'Controleur de pc', home: Remote());
//   }
// }

//void main() => runApp(const MaterialApp(title: 'Controleur de pc', home: Remote()));

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return const
//   }
// }

class computer_chose extends StatefulWidget {
  final String url;
  information infos;

  computer_chose({Key? key, required this.url, required this.infos})
      : super(key: key);

  @override
  State<computer_chose> createState() => _computer_choseState();
}

class _computer_choseState extends State<computer_chose> {
  List<dynamic> devices = <dynamic>[];
  bool fetched = false;
  void snackBarMessage(String msg){
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content:  Text(msg),
      duration: const Duration(seconds: 5),
      // action: SnackBarAction(
      //   label: 'ACTION',
      //   onPressed: () { },
      // ),
    ));
  }

  ///retreive all device of the connected user
  void getAllDevices() async {
    try {
      log(widget.url);
      log("token actuel : \n"+widget.infos.token);

      final response = await
      get(Uri.parse(widget.url + "/device/getAll"),
          headers: {"x-access-token": widget.infos.token});

      final jsonData = jsonDecode(response.body);


      ///if token expired
      if(response.statusCode == 401){
        log("token expir??");
        log( widget.infos.refreshToken["token"]);
        var refresh = await post(Uri.parse(widget.url+"/refreshToken"),body: {
          "refreshToken" : widget.infos.refreshToken["token"]
        });
        final jsonToken = jsonDecode(refresh.body);
        log(refresh.body);
        log(refresh.statusCode.toString());
        ///if refresh token has expired
        if(refresh.statusCode ==200){
          log("token r??cup??r??");
          snackBarMessage("Token r??cup??r??, reload");

            widget.infos.setToken(jsonToken["accessToken"]);
            widget.infos.updateJson();

        }

        if(refresh.statusCode == 403){
          log("refresh espir??");
          showAlertDialog(context, "Token expired, please login again","Get device",sign: true);
        }else {

          snackBarMessage(jsonToken["message"]);
        }


      }


      // log("success");
      // log(response.statusCode.toString());
      // log(response.body);
      //
      // log(jsonData["message"]);
      log(response.statusCode.toString());
      if(response.statusCode == 200) {
        log("yesyesyes");
        setState(() {
          devices = jsonData["devices"];
          fetched = true;
        });
      }else {
        log(response.body);
        snackBarMessage(jsonData["message"]);
      }
    } catch (err) {
      log(err.toString());
      //return err.toString();
    }
  }

  List<Widget> allComputer() {
    if (!fetched) {
      getAllDevices();
    }
    // List<Widget> list = List.generate(10, (index) => null);
    var list = <Widget>[];
    list.add(SizedBox(height: 10));
    list.add(Text(
      "Number of devices : " + devices.length.toString(),
      style: TextStyle(color: Colors.white, fontSize: 18),
    ));
    for (var device in devices) {
      list.add(computer(device));
    }
    return list;
  }

  void refreshData(dynamic value) {
    fetched = false;
    getAllDevices();
  }

  Widget computer(computer_info) {
    String online;
    online = (computer_info["isOnline"]) ? "Connected" : "Disconnected";



    //log("online : "+computer_info["isOnline"]);
    return Container(
      padding: EdgeInsets.symmetric(vertical: 10),
      width: double.infinity,
      child: RaisedButton(
        elevation: 5,
        onPressed: () => {
          // Navigator.of(context).(MaterialPageRoute(
          //     builder: (context)=>Remote()
          // ))
          widget.infos.computerId = computer_info["uuid"],
          widget.infos.computerName = computer_info["name"],
          Navigator.push(context, MaterialPageRoute(builder: (context)=> Remote(url : widget.url, infos : widget.infos))).then(refreshData )



        },
        padding: EdgeInsets.all(10),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
        color: Colors.white,
        child: Column(
          children: [
            Text(
              'Name : ' + computer_info["name"],
              style: TextStyle(
                  color: Colors.blue,
                  fontSize: 18,
                  fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 10),
            Text(
              online,
              style: TextStyle(
                  color: (computer_info["isOnline"]) ? Colors.green : Colors.red,
                  fontSize: 18,
                  fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Chose device'),
        ),
        floatingActionButton: FloatingActionButton.extended(
          onPressed: () {
            setState(() {
              fetched = false;
            });
          },
          icon: const Icon(Icons.rotate_right_rounded),
          label: const Text('Reload'),
        ),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
        body: AnnotatedRegion<SystemUiOverlayStyle>(
            value: SystemUiOverlayStyle.light,
            child: GestureDetector(
                child: Stack(children: <Widget>[
                  Container(
                    height: double.infinity,
                    width: double.infinity,
                    decoration: BoxDecoration(
                        gradient: LinearGradient(
                            begin: Alignment.topCenter,
                            end: Alignment.bottomCenter,
                            colors: [
                              Colors.blue,
                              Colors.blue[300]!,
                              Colors.blue[100]!,
                            ])),
                    child: SingleChildScrollView(
                      padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                      child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: allComputer()),
                    ),
                  ),
                ]))));
  }
}
