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


class Remote extends StatefulWidget {
  final String url;
  information infos;


  Remote({Key? key, required this.url, required this.infos}) : super(key: key);

  @override
  State<Remote> createState() => _RemoteState();
}

class _RemoteState extends State<Remote> {
  String label = "Server answer here";

  showShutDownDialog() {

    // set up the button


    // set up the AlertDialog
    AlertDialog alert = AlertDialog(
      title: Text("Shutdown"),
      content: Text("Are you sure you want to shutdown your device ?"),
      actions: [
        TextButton( onPressed: () {  requete(7); Navigator.of(context).pop();}, child: Text("yes")),
        TextButton( onPressed: () {  Navigator.of(context).pop(); }, child: Text("no")),



      ],
    );

    // show the dialog
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alert;
      },
    );
  }

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

  /// state : 1- up , 2-down, 3-mute, 4-unmute, 5-play, 6-pause , 7-shutdown, 8 skip previous, 9 skip next 10 lock, 11 arrow up, 12 Adown , 13 Aleft 14 A right
  void requete(int state) async {
    String message = "";
    String request = "";
    switch (state) {
      case 1:
        message = "up - ";
        request = "/volume/up/" + widget.infos.computerId.toString();
        break;
      case 2:
        request = "/volume/down/" + widget.infos.computerId.toString();
        message = "down - ";

        break;
      case 3:
        request = "/volume/mute/" + widget.infos.computerId.toString();
        message = "mute - ";

        break;
      case 4:
        request = "/volume/unmute/" + widget.infos.computerId.toString();
        message = "unmute - ";

        break;
      case 5:
        request = "/volume/play/" + widget.infos.computerId.toString();
        message = "play - ";

        break;
      case 6:
        request = "/volume/pause/" + widget.infos.computerId.toString();
        message = "pause - ";

        break;
      case 7:
        request = "/shutdown/" + widget.infos.computerId.toString();
        message = "shutdown - ";
        break;
      case 8:
        request = "/previous-music/" + widget.infos.computerId.toString();
        message = "previous-music - ";
        break;
      case 9:
        request = "/next-music/" + widget.infos.computerId.toString();
        message = "next-music - ";
        break;
      case 10:
        request = "/lock/" + widget.infos.computerId.toString();
        message = "lock - ";
        break;
      case 11:
        request = "/arrow/up/" + widget.infos.computerId.toString();
        message = "arrow up - ";
        break;
      case 12:
        request = "/arrow/down/" + widget.infos.computerId.toString();
        message = "arrow down - ";
        break;
      case 13:
        request = "/arrow/left/" + widget.infos.computerId.toString();
        message = "arrow left - ";
        break;
      case 14:
        request = "/arrow/right/" + widget.infos.computerId.toString();
        message = "arrow right - ";
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
            Navigator.push(context, MaterialPageRoute(builder: (context) =>
                editDevice(url: widget.url, infos: widget.infos)));
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
                  Text('Device : ' + widget.infos.computerName!,
                      style: TextStyle(fontSize: 20,
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
                              showShutDownDialog();
                            },
                          ),
                        ),
                      ],
                    ),
                  ),
                  //flèche haut
                  SizedBox(
                    height: 50,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Transform.scale(
                          scale: 3,
                          child: RotatedBox(
                            quarterTurns: 1,
                            child: IconButton(
                              icon: const Icon(Icons.arrow_back_ios_sharp),
                              color: Colors.white,
                              onPressed: () {
                                requete(11);
                              },
                            ),
                          ),
                        ),

                      ],
                    ),
                  ),

                  ///flèches /
                  SizedBox(
                    height: 40,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        Transform.scale(
                          scale: 3,
                          child: IconButton(
                            icon: const Icon(Icons.arrow_back_ios_sharp),
                            color: Colors.white,
                            onPressed: () {
                              requete(13);
                            },
                          ),
                        ),


                        Transform.scale(
                          scale: 3,
                          child: RotatedBox(
                            quarterTurns: 2,
                            child: IconButton(
                              icon: const Icon(Icons.arrow_back_ios_sharp),
                              color: Colors.white,
                              onPressed: () {
                                requete(14);
                              },
                            ),
                          ),
                        ),

                      ],
                    ),
                  ),

                        SizedBox(
                          height: 50,
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                            children: [

                              Transform.scale(
                                scale: 3,
                                child: RotatedBox(
                                  quarterTurns: 3,
                                  child: IconButton(
                                    icon: const Icon(
                                        Icons.arrow_back_ios_sharp),
                                    color: Colors.white,
                                    onPressed: () {
                                      requete(12);
                                    },
                                  ),
                                ),
                              ),


                            ],
                          ),
                        ), //
                        SizedBox(height: 30.0),
                        Text('$label', style: TextStyle(fontSize: 20,
                            color: Colors.white)),




                      ],

                    ),
                  ),
            ),
                ],
                  ),
                ),
              ),
                );
  }
}
