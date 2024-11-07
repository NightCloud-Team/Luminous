package com.example.luminous

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.activity.ComponentActivity
import androidx.activity.enableEdgeToEdge
import com.luminous.luminous.R

class main : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.main)
        Handler(Looper.getMainLooper()).postDelayed({
            val intent = Intent(this, quickmenu::class.java)
            startActivity(intent)
            finish() // 可选，结束当前活动
        }, 3000)
    }
}
