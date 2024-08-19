import 'package:dartz/dartz.dart';
import 'package:spotify/core/usecase/usecase.dart';
import 'package:spotify/data/models/auth/new_user.dart';
import 'package:spotify/domain/repository/auth_repo/auth.dart';
import 'package:spotify/service_locator.dart';

class SignupUseCase implements UseCase<Either, NewUser> {
  @override
  Future<Either> call({NewUser? params}) {
    return serviceLocator<AuthRepository>().signup(params!);
  }
}
