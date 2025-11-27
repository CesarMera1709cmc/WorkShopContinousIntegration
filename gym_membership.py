"""
Gym Membership Management System
Sistema de Gestión de Membresías de Gimnasio
"""


class GymMembership:
    """Clase principal para manejar las membresías del gimnasio"""
    
    # Planes de membresía disponibles
    MEMBERSHIP_PLANS = {
        "Basic": {
            "cost": 50,
            "benefits": ["Acceso a área de pesas", "Vestidores"]
        },
        "Premium": {
            "cost": 100,
            "benefits": ["Acceso a área de pesas", "Vestidores", "Sauna", "Piscina"]
        },
        "Family": {
            "cost": 150,
            "benefits": ["Acceso familiar hasta 4 personas", "Todas las áreas", "Clases grupales incluidas"]
        }
    }
    
    # Características adicionales disponibles
    ADDITIONAL_FEATURES = {
        "Personal Training": 40,
        "Group Classes": 25,
        "Nutrition Consultation": 30,
        "Locker Rental": 10
    }
    
    # Características premium
    PREMIUM_FEATURES = {
        "Exclusive Gym Access": 80,
        "Specialized Training Program": 60
    }
    
    def __init__(self):
        """Inicializa el sistema de membresías"""
        self.selected_plan = None
        self.additional_features = []
        self.premium_features = []
        self.num_members = 1
        self.total_cost = 0
    
    def display_membership_plans(self):
        """Muestra los planes de membresía disponibles"""
        print("\n" + "="*60)
        print("PLANES DE MEMBRESÍA DISPONIBLES")
        print("="*60)
        for plan_name, details in self.MEMBERSHIP_PLANS.items():
            print(f"\n{plan_name}: ${details['cost']}/mes")
            print("Beneficios:")
            for benefit in details['benefits']:
                print(f"  - {benefit}")
        print("="*60 + "\n")
    
    def select_membership_plan(self, plan_name):
        """
        Selecciona un plan de membresía
        
        Args:
            plan_name: Nombre del plan a seleccionar
            
        Returns:
            bool: True si la selección fue exitosa, False si no
        """
        if plan_name not in self.MEMBERSHIP_PLANS:
            print(f"Error: El plan '{plan_name}' no está disponible.")
            return False
        
        self.selected_plan = plan_name
        print(f"✓ Plan '{plan_name}' seleccionado exitosamente.")
        return True
    
    def add_additional_feature(self, feature_name):
        """
        Agrega una característica adicional
        
        Args:
            feature_name: Nombre de la característica a agregar
            
        Returns:
            bool: True si se agregó exitosamente, False si no
        """
        if feature_name not in self.ADDITIONAL_FEATURES:
            print(f"Error: La característica '{feature_name}' no está disponible.")
            return False
        
        self.additional_features.append(feature_name)
        print(f"✓ Característica '{feature_name}' agregada.")
        return True
    
    def add_premium_feature(self, feature_name):
        """
        Agrega una característica premium
        
        Args:
            feature_name: Nombre de la característica premium
            
        Returns:
            bool: True si se agregó exitosamente, False si no
        """
        if feature_name not in self.PREMIUM_FEATURES:
            print(f"Error: La característica premium '{feature_name}' no está disponible.")
            return False
        
        self.premium_features.append(feature_name)
        print(f"✓ Característica premium '{feature_name}' agregada.")
        return True
    
    def set_number_of_members(self, num):
        """
        Establece el número de miembros para descuento grupal
        
        Args:
            num: Número de miembros
            
        Returns:
            bool: True si es válido, False si no
        """
        if num < 1:
            print("Error: El número de miembros debe ser al menos 1.")
            return False
        
        self.num_members = num
        return True
    
    def calculate_base_cost(self):
        """
        Calcula el costo base de la membresía
        
        Returns:
            float: Costo base de la membresía seleccionada
        """
        if not self.selected_plan:
            return 0
        return self.MEMBERSHIP_PLANS[self.selected_plan]["cost"]
    
    def calculate_additional_features_cost(self):
        """
        Calcula el costo de las características adicionales
        
        Returns:
            float: Costo total de características adicionales
        """
        total = 0
        for feature in self.additional_features:
            total += self.ADDITIONAL_FEATURES[feature]
        return total
    
    def calculate_premium_features_cost(self):
        """
        Calcula el costo de las características premium
        
        Returns:
            float: Costo total de características premium
        """
        total = 0
        for feature in self.premium_features:
            total += self.PREMIUM_FEATURES[feature]
        return total
    
    def apply_group_discount(self, subtotal):
        """
        Aplica descuento del 10% si hay 2 o más miembros
        
        Args:
            subtotal: Subtotal antes del descuento
            
        Returns:
            float: Descuento aplicado
        """
        if self.num_members >= 2:
            discount = subtotal * 0.10
            print(f"✓ Descuento grupal aplicado (10%): -${discount:.2f}")
            return discount
        return 0
    
    def apply_special_offer_discount(self, subtotal):
        """
        Aplica descuentos especiales según el total
        - Si excede $200: descuento de $20
        - Si excede $400: descuento de $50
        
        Args:
            subtotal: Subtotal antes del descuento
            
        Returns:
            float: Descuento aplicado
        """
        if subtotal > 400:
            print("✓ Descuento especial aplicado: -$50")
            return 50
        elif subtotal > 200:
            print("✓ Descuento especial aplicado: -$20")
            return 20
        return 0
    
    def apply_premium_surcharge(self, subtotal):
        """
        Aplica recargo del 15% si hay características premium
        
        Args:
            subtotal: Subtotal antes del recargo
            
        Returns:
            float: Recargo aplicado
        """
        if len(self.premium_features) > 0:
            surcharge = subtotal * 0.15
            print(f"✓ Recargo premium aplicado (15%): +${surcharge:.2f}")
            return surcharge
        return 0
    
    def calculate_total_cost(self):
        """
        Calcula el costo total de la membresía con todos los descuentos y recargos
        
        Returns:
            float: Costo total final
        """
        if not self.selected_plan:
            print("Error: No se ha seleccionado un plan de membresía.")
            return -1
        
        # Costo base
        base_cost = self.calculate_base_cost()
        
        # Costo de características adicionales
        additional_cost = self.calculate_additional_features_cost()
        
        # Costo de características premium
        premium_cost = self.calculate_premium_features_cost()
        
        # Subtotal antes de descuentos
        subtotal = base_cost + additional_cost + premium_cost
        
        print(f"\nCosto base de membresía: ${base_cost}")
        print(f"Características adicionales: ${additional_cost}")
        print(f"Características premium: ${premium_cost}")
        print(f"Subtotal: ${subtotal}")
        
        # Aplicar descuento grupal
        group_discount = self.apply_group_discount(subtotal)
        
        # Aplicar descuento especial
        special_discount = self.apply_special_offer_discount(subtotal)
        
        # Calcular total después de descuentos
        total_after_discounts = subtotal - group_discount - special_discount
        
        # Aplicar recargo premium
        premium_surcharge = self.apply_premium_surcharge(total_after_discounts)
        
        # Total final
        self.total_cost = total_after_discounts + premium_surcharge
        
        return round(self.total_cost, 2)
    
    def display_summary(self):
        """Muestra un resumen de la membresía seleccionada"""
        print("\n" + "="*60)
        print("RESUMEN DE MEMBRESÍA")
        print("="*60)
        print(f"Plan seleccionado: {self.selected_plan}")
        print(f"Número de miembros: {self.num_members}")
        
        if self.additional_features:
            print("\nCaracterísticas adicionales:")
            for feature in self.additional_features:
                print(f"  - {feature} (${self.ADDITIONAL_FEATURES[feature]})")
        
        if self.premium_features:
            print("\nCaracterísticas premium:")
            for feature in self.premium_features:
                print(f"  - {feature} (${self.PREMIUM_FEATURES[feature]})")
        
        print(f"\nCosto total: ${self.total_cost:.2f}")
        print("="*60 + "\n")
    
    def confirm_membership(self):
        """
        Confirma la membresía y retorna el costo total
        
        Returns:
            int: Costo total como entero positivo si es válido, -1 si no
        """
        if not self.selected_plan:
            print("Error: No hay plan seleccionado para confirmar.")
            return -1
        
        self.display_summary()
        
        print("¿Desea confirmar esta membresía? (s/n): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation == 's' or confirmation == 'si' or confirmation == 'yes':
            print("\n✓ Membresía confirmada exitosamente.")
            return int(self.total_cost) if self.total_cost > 0 else -1
        else:
            print("\n✗ Membresía cancelada.")
            return -1


def main():
    """Función principal para ejecutar el programa de manera interactiva"""
    gym = GymMembership()
    
    print("\n" + "="*60)
    print("BIENVENIDO AL SISTEMA DE MEMBRESÍAS DEL GIMNASIO")
    print("="*60)
    
    # Mostrar planes disponibles
    gym.display_membership_plans()
    
    # Seleccionar plan
    print("Planes disponibles: Basic, Premium, Family")
    plan = input("Seleccione un plan de membresía: ").strip()
    
    if not gym.select_membership_plan(plan):
        print("Proceso cancelado.")
        return -1
    
    # Número de miembros
    try:
        num_members = int(input("\n¿Cuántos miembros se inscribirán juntos? (mínimo 1): "))
        if not gym.set_number_of_members(num_members):
            print("Proceso cancelado.")
            return -1
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return -1
    
    # Características adicionales
    print("\nCaracterísticas adicionales disponibles:")
    for feature, cost in gym.ADDITIONAL_FEATURES.items():
        print(f"  - {feature}: ${cost}")
    
    print("\n¿Desea agregar características adicionales? (s/n): ", end="")
    if input().strip().lower() in ['s', 'si', 'yes']:
        print("Ingrese las características separadas por coma (o presione Enter para omitir):")
        features_input = input().strip()
        if features_input:
            for feature in features_input.split(','):
                gym.add_additional_feature(feature.strip())
    
    # Características premium
    print("\nCaracterísticas premium disponibles:")
    for feature, cost in gym.PREMIUM_FEATURES.items():
        print(f"  - {feature}: ${cost}")
    
    print("\n¿Desea agregar características premium? (s/n): ", end="")
    if input().strip().lower() in ['s', 'si', 'yes']:
        print("Ingrese las características premium separadas por coma (o presione Enter para omitir):")
        features_input = input().strip()
        if features_input:
            for feature in features_input.split(','):
                gym.add_premium_feature(feature.strip())
    
    # Calcular costo total
    total = gym.calculate_total_cost()
    
    if total == -1:
        print("Error en el cálculo.")
        return -1
    
    # Confirmar membresía
    result = gym.confirm_membership()
    
    return result


if __name__ == "__main__":
    main()
