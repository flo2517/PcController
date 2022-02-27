// ignore_for_file: prefer_const_constructors

import 'dart:convert';
import 'dart:developer';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app/pages/edit_device.dart';
import 'package:http/http.dart';
import '../information.dart';
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

class Remote extends StatefulWidget {
  final String url;
  information infos;


   Remote({Key? key , required this.url, required this.infos}) : super(key: key);

  @override
  State<Remote> createState() => _RemoteState();
}

class _RemoteState extends State<Remote> {
  String label = "Server answer here";
  // final id = 1234;
  //
  // final url = "http://192.168.1.33:8080";

  Future<String> fetchPosts(String request) async {
    try {
      final response = await get(Uri.parse(widget.url + request),
          headers: {"x-access-token": widget.infos.token});
      final jsonData = jsonDecode(response.body);
      log("success");
      log(response.statusCode.toString());
      log(response.body);
      log(jsonData["message"]);
      return jsonData["message"] +
          " - code : " +
          response.statusCode.toString();
    } catch (err) {
      log(err.toString());
      return err.toString();
    }
  }

  /// state : 1- up , 2-down, 3-mute, 4-unmute, 5-play, 6-pause , 7-shutdown, 8 skip previous, 9 skip next
  void requete(int state) async {
    String message = "";
    String request = "";
    switch (state) {
      case 1:
        message = "up - ";
        request = "/volume/up/" + widget.infos.computerId.toString();
        break;
      case 2:
        request = "/volume/down/" +  widget.infos.computerId.toString();
        message = "down - ";

        break;
      case 3:
        request = "/volume/mute/" +  widget.infos.computerId.toString();
        message = "mute - ";

        break;
      case 4:
        request = "/volume/unmute/" +  widget.infos.computerId.toString();
        message = "unmute - ";

        break;
      case 5:
        request = "/volume/play/" +  widget.infos.computerId.toString();
        message = "play - ";

        break;
      case 6:
        request = "/volume/pause/" +  widget.infos.computerId.toString();
        message = "pause - ";

        break;
      case 7:
        request = "/shutdown/" +  widget.infos.computerId.toString();
        message = "shutdown - ";
        break;
      case 8:
        request = "/previous-music/" +  widget.infos.computerId.toString();
        message = "previous-music - ";
        break;
      case 9:
        request = "/next-music/" +  widget.infos.computerId.toString();
        message = "next-music - ";
        break;
      case 10:
        request = "/lock/" +  widget.infos.computerId.toString();
        message = "lock - ";
        break;
      default:
        break;
    }
    message += await fetchPosts(request);

    setState(() {
      label = message;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Pc controller'),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          Navigator.push(context, MaterialPageRoute(builder: (context)=> editDevice(url : widget.url, infos : widget.infos)));

        },
        icon: const Icon(Icons.edit),
        label: const Text('Edit device'),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      body: AnnotatedRegion<SystemUiOverlayStyle>(
        value: SystemUiOverlayStyle.light,
        child: GestureDetector(
          child: Stack(
            children: <Widget>[
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
             // padding: EdgeInsets.symmetric(horizontal: 25, vertical: 120),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  SizedBox(height: 20.0),
                  Text('Device : '+widget.infos.computerName!, style: TextStyle(fontSize: 20,
                      color: Colors.white)),
                  SizedBox(
                    height: 100,


                    ///volume
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: <Widget>[
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.volume_off_rounded),
                            color: Colors.white,
                            onPressed: () {
                              requete(3);
                            },
                          ),
                        ),
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.volume_down_rounded),
                            color: Colors.white,
                            onPressed: () {
                              requete(2);
                            },
                          ),
                        ),
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.volume_up_rounded),
                            color: Colors.white,
                            onPressed: () {
                              requete(1);
                            },
                          ),
                        ),
                      ],
                    ),
                  ),
                  ///play pause
                  // SizedBox(
                  //   height: 100,
                  //   child: Row(
                  //     mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  //     children: [
                  //       Transform.scale(
                  //         scale: 3,
                  //         child: IconButton(
                  //           icon: const Icon(Icons.play_circle_outline_rounded),
                  //           onPressed: () {
                  //             requete(5);
                  //           },
                  //         ),
                  //       ),
                  //       Transform.scale(
                  //         scale: 3,
                  //         child: IconButton(
                  //           icon: const Icon(Icons.pause_circle_outline_rounded),
                  //           onPressed: () {
                  //             requete(6);
                  //           },
                  //         ),
                  //       ),
                  //     ],
                  //   ),
                  // ),
                  ///previous, play/pause next
                  SizedBox(
                    height: 100,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.skip_previous_rounded),
                            color: Colors.white,
                            onPressed: () {
                              requete(8);
                            },
                          ),
                        ),
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.play_circle_outline_rounded),
                            color: Colors.white,
                            onPressed: () {
                              requete(6);
                            },
                          ),
                        ),
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.skip_next_rounded),
                            color: Colors.white,
                            onPressed: () {
                              requete(9);
                            },
                          ),
                        ),
                      ],
                    ),
                  ),
                 ///lock shutdown
                  SizedBox(
                    height: 100,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.lock_outline_rounded),
                            color: Colors.white,
                            onPressed: () {
                              requete(10);
                            },
                          ),
                        ),
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.power_settings_new_rounded),
                            color: Colors.white,
                            onPressed: () {
                              requete(7);

                              // showDialog(
                              //     context: context,
                              //     barrierDismissible: false,
                              //
                              //     builder: (_) =>
                              //         CupertinoAlertDialog(
                              //           title: Text("clique"),
                              //           //content: Text("fezgzge"),
                              //           actions:
                              //             <Widget>[
                              //               CupertinoDialogAction(
                              //                 child: Text('ok'),
                              //                 onPressed: () {
                              //                   Navigator.of(context).pop();
                              //                 },
                              //               ),
                              //
                              //             ],
                              //
                              //         )
                              // );
                            },
                          ),
                        ),
                      ],
                    ),
                  ), //
                  SizedBox(height: 10.0),
                  Text('$label', style: TextStyle(fontSize: 20,
                  color: Colors.white)),

                  // Align(
                  //   alignment: Alignment.bottomLeft,
                  //   child: TextButton(
                  //     onPressed: () {},
                  //     child: Text(
                  //       "Changer d'appareil",
                  //       style: TextStyle(
                  //           color: Colors.black,
                  //           fontSize: 18,
                  //           fontWeight: FontWeight.w500),
                  //     ),
                  //   ),
                  // ),



                ],
              ),
            ),
          ),
      ]),
        ),
      ));
  }
}
