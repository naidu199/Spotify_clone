// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'dart:convert';

class NewUser {
  final String email;
  final String name;
  final String password;

  NewUser({required this.email, required this.name, required this.password});

  Map<String, dynamic> toMap() {
    return <String, dynamic>{
      'email': email,
      'name': name,
      'password': password,
    };
  }

  factory NewUser.fromMap(Map<String, dynamic> map) {
    return NewUser(
      email: map['email'] as String,
      name: map['name'] as String,
      password: map['password'] as String,
    );
  }

  String toJson() => json.encode(toMap());

  factory NewUser.fromJson(String source) =>
      NewUser.fromMap(json.decode(source) as Map<String, dynamic>);
}
