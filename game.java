import java.awt.event.KeyEvent;
import java.awt.event.KeyAdapter;
import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.Graphics;
import  javax.swing.Timer;
import java.awt.ActiveEvent;
import java.awt.event.ActionListener;

public class Main {
    public static void main(String []args){

        //視窗
        JFrame window = new JFrame(); //建立視窗物件
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //按下x關閉
        window.setResizable(false); //無法改變大小
        window.setTitle("game"); //名稱
        window.setSize(1400,800); //大小
        window.setLocationRelativeTo(null); //正中央

        //畫板
        GamePanel gamePanel = new GamePanel(); //建立畫板
        window.add(gamePanel); //畫板放進視窗
        window.pack(); //畫板=視窗

        window.setVisible(true); //顯示
        System.out.println("window");

        gamePanel.requestFocus();

    }
}
//-------------------------------------------------------------------------
//自訂畫板
class GamePanel extends JPanel {

    //player
    int x = 687; //初始位子
    int y = 700;
    int size = 25; //方塊大小
    int speed = 10; //每次移動距離

    public GamePanel() {
        this.setPreferredSize(new Dimension(1400, 800)); //畫板大小
        this.setBackground(Color.darkGray); //顏色

        this.setFocusable(true);//鍵盤有反應
        this.requestFocusInWindow();

        //加入鍵盤監聽
        this.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e){
                int code = e.getKeyCode();
                System.out.println( code); // 測試用
           //移動
           if (code == KeyEvent.VK_W) y -= speed;
           if (code == KeyEvent.VK_S) y += speed;
           if (code == KeyEvent.VK_A) x -= speed;
           if (code == KeyEvent.VK_D) x += speed;
           // 防止出界邏輯
            if (x < 0) x = 0;
            if (y < 0) y = 0;
            if (x > 1400 - size) x = 1400 - size;
            if (y > 800 - size) y = 800 - size;

            repaint(); //重新繪製
            }
        });
    }



     //畫圖
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        g.setColor(Color.green); //顏色
        g.fillRect(x,y,size,size); //(X,Y,H,W)
    }
}