import 'package:dartz/dartz.dart';
import 'package:spotify/data/models/auth/check_user.dart';
import 'package:spotify/data/models/auth/new_user.dart';
import 'package:spotify/data/source/auth/auth_firebase_service.dart';
import 'package:spotify/domain/repository/auth_repo/auth.dart';
import 'package:spotify/service_locator.dart';

class AuthRepoImpl extends AuthRepository {
  @override
  Future<Either> signin(CheckUser user) async {
    return await serviceLocator<AuthFirebase>().signin(user);
  }

  @override
  Future<Either> signup(NewUser newUser) async {
    return await serviceLocator<AuthFirebase>().signup(newUser);
  }
}
