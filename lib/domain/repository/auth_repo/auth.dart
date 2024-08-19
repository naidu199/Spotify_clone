import 'package:dartz/dartz.dart';
import 'package:spotify/data/models/auth/check_user.dart';
import 'package:spotify/data/models/auth/new_user.dart';

abstract class AuthRepository {
  Future<Either> signup(NewUser newUser);
  Future<Either> signin(CheckUser user);
}
