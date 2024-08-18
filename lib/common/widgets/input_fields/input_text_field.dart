import 'package:flutter/material.dart';
import 'package:spotify/core/config/theme/app_colors.dart';

class InputTextField extends StatelessWidget {
  final TextEditingController? controller;
  final String hintText;
  final String? label;
  final IconData? prefixIcon;

  const InputTextField(
      {super.key,
      this.controller,
      required this.hintText,
      this.label,
      this.prefixIcon});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 16.0),
      child: TextFormField(
        controller: controller,
        decoration: InputDecoration(
          prefixIcon: Icon(prefixIcon),
          hintText: hintText,
          hintStyle: const TextStyle(
            fontWeight: FontWeight.w600,
            fontSize: 16,
          ),
          filled: true,
          fillColor: Colors.transparent,
          border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(15),
              borderSide: const BorderSide(width: 2)),
          focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(15),
              borderSide: const BorderSide(color: AppColors.primary)),
        ),
      ),
    );
  }
}
