public class CombatProgram
{
	public static void main(String[] args)
	{
		//Create the player
		Character player = new Character();
		player.name = "Wizard";
		player.health = 100;
		player.damage = 25;

		//Create the enemy
		Character enemy = new Character();
		player.name = "Zombie";
		player.health = 100;
		player.damage = 25;

		//Player attacks enemy
		player.attackCharacter(enemy);
	}
}
